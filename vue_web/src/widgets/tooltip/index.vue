<template>
  <div class="text-truncate-tooltip">
    <Tooltip :content="content"
     :max-width="ratioMaxWidth"
     :transfer="true" 
     :disabled="disableTooltip || content.length === 0"
     :style="textStyle"
      placement="top">
      <div v-if="singleLine" class="text-truncate" ref="content" @mouseenter="updateComponent">
        {{ content }}
      </div>
      <div v-else :class="{'multiline-overflow-truncate': multilineTruncated, 'multiline-content': true}" ref="content" :style="textStyle" @mouseenter="updateComponent">
        {{ content }}
      </div>
    </Tooltip>
  </div>
</template>
<script lang="ts">
import Vue, { PropType } from 'vue';

const FONT_SIZE = '14px';
const LINE_HEIGHT = '1.5';
export default Vue.extend({
  name: 'text-truncate-tooltip',
  props: {
    content: { type: String, default: '' },
    maxWidth: { type: Number, default: 240},
    ratio: {type: Number, default: 1.08},
    maxLineCount: { type: Number, default: 1 },
  },
  data() {
    return {
      disableTooltip: false as boolean,
      textStyle: {} as any,
      ratioMaxWidth: this.maxWidth,
      multilineTruncated: false as boolean,
    };
  },
  methods: {
    async updateComponent() {
      const vm: any = this;
      const element: any = vm.$refs.content;
      // update css
      const computedLineHeight = window.getComputedStyle(element).getPropertyValue('line-height');
      vm.textStyle = {
        'width': vm.maxWidth + 'px',
        'max-height': vm.singleLine ? 'auto' : `calc(${computedLineHeight} * ${vm.maxLineCount})`,
      };
      // update functions
      vm.disableTooltip = !(vm.isOverflowX() || vm.isOverflowY());
      vm.ratioMaxWidth = element.clientWidth * vm.ratio;
      vm.multilineTruncated = vm.isOverflowY();
    },
    isOverflowX(): boolean {
      const vm: any = this;
      const element: any = vm.$refs.content;
      if (element) {
        return element.clientWidth < element.scrollWidth;
      } else {
        return false;
      }
    },
    isOverflowY(): boolean {
      const vm: any = this;
      const element: any = vm.$refs.content;
      if (element) {
        return element.clientHeight < element.scrollHeight;
      } else {
        return false;
      }
    },
  },
  computed: {
    singleLine(): boolean {
      const vm: any = this;
      return vm.maxLineCount === 1;
    },
  },
  mounted() {
    const vm: any = this;
    vm.updateComponent();
  },


});
</script>
<style scoped lang="less">
.multiline-content {
//  --max-lines: 3;
  position: relative;
//  max-height: calc(1.5 * 14px * var(--max-lines)); /* line-height * font-size * max-lines */
  overflow: hidden;
  padding-right: 1rem; /* space for ellipsis */
}
.multiline-overflow-truncate::before {
  position: absolute;
  content: "...";
  bottom: 0; /* "bottom" */
  right: 0; /* "right" */
}
</style>

