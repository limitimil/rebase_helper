<template>
  <div class="editable-repository-record-root d-flex">
    <div class="operation d-inline hack2 " @click="toggle">
      <!-- TODO: make font awsome icon as a component to save typing-->
      <i class="btn" :class="classOperationIcon"/>
    </div>
    <div class="content hack3">
      <div class="fields-wrapper" :class="classFieldsWrapper">
        <div class="fields" :class="classFields">
          <label class="d-inline" for="">repository url</label>
          <TextTruncateTooltip :content="url" class="field-content" v-if="flagMode.View"/>
          <Input class="field-content" v-model="url" v-if="flagMode.Edit"></Input>
        </div>
        <div class="fields" :class="classFields">
          <label class="d-inline" for="">branches</label>
          <!-- TODO: should be filtered to be comma seperate format-->
          <div class="field-content" v-if="flagMode.View">{{ branches }}</div>
          <AutoElementSelect class="field-content" :value.sync="branches" v-if="flagMode.Edit"></AutoElementSelect>
        </div>
        <div class="fields" :class="classFields" v-if="flagMode.Edit">
          <label class="d-inline" for="">plugins</label>
          <!-- TODO: should be filtered to be formated json-->
          <Input class="field-content" v-model="plugins" :disabled="!flagMode.Edit" :readonly="!flagMode.Edit" type="textarea"></Input>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue, { PropType } from 'vue';
import TextTruncateTooltip from '@/widgets/tooltip';
import AutoElementSelect from '@/widgets/select';

enum EnumMode{
  Edit,
  View
};

export default Vue.extend({
  name: 'New-Component',
  props: { 
    url: { type: String, default: '' },
    branches: { type: Array, default: () => [] },
  }, 
  components: {
    TextTruncateTooltip,
    AutoElementSelect
  },
  data() {
    return {
      helloworold: 'helloworld' as string,
      mode: EnumMode.View as EnumMode,
    };
  },
  methods: {
    toggle() {
      const vm: any=this;
      switch(vm.mode){
        case EnumMode.Edit:
          vm.mode = EnumMode.View;
          break;
        case EnumMode.View:
          vm.mode = EnumMode.Edit;
          break;
      }
    }
  },
  computed: {
    flagMode() {
      const vm: any=this;
      return {
        Edit: vm.mode === EnumMode.Edit,
        View: vm.mode === EnumMode.View,
      };
    },
    classOperationIcon() {
      const vm: any=this;
      if (vm.mode === EnumMode.Edit) {
        return 'fas fa-save';
      }
      return 'fas fa-edit';
    },
    classFields() {
      const vm: any=this;
      switch(vm.mode){
        case EnumMode.Edit:
          return 'd-flex col-4';
        case EnumMode.View:
          return 'd-flex col-6';
      }
    },
    classFieldsWrapper() {
      return 'row';
    },
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
.fields {
  *{
    padding-right: 1em;
  }
}
.content {
  width: 100%;
}
</style>

