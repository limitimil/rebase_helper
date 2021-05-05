<template>
  <Select v-model="value" allow-create multiple filterable>
    <Option v-for="(option, index) in options" :value="option.value" :key="index">{{option.label}}</Option>
  </Select>
</template>
<script lang="ts">
import Vue, { PropType } from 'vue';
import mixins from 'vue-typed-mixins';
import { ValueSync } from '@/mixins';

export default mixins(ValueSync).extend({
  name: 'auto-element-select-list',
  props: {
    value: { type: Array, default: () => [] },
  },
  components: {
  },
  data() {
    return {
      options: [] as any[],
    };
  },
  methods: {
    renderOptions(){
      const vm: any=this;
      return vm.value.map( (element: str) => {
        return {
          value: element,
          key: element,
          label: element,
        };
      });
    },
  },
  created(){
    this.$set(this, "options", this.renderOptions());
  },
});
</script>
<style scoped lang="less">
.hack1{
 background-color: hsla(208, 26%, 75%, 1);
}
.hack2{
 background-color: hsla(17, 25%, 33%, 1);
}
.hack3{
 background-color: hsla(203, 16%, 96%, 1);
}
.hack4{
 background-color: hsla(214, 15%, 62%, 1);
}
.hack5{
 background-color: hsla(240, 7%, 47%, 1);
}
</style>

