<template>
  <div class="editable-repository-record-root hack1">
    <div class="operation d-inline-block hack2 ">
      <div class="btn">{{operation}}</div>
    </div>
    <div class="content d-inline-block hack3">
      <div class="fields-wrapper" :class="classFieldsWrapper">
        <div class="fields" :class="classFields">
          <label for="">repository url</label>
          <div class="content">{{url}}</div>
          <Input class="content" v-model="url"></Input>
        </div>
        <div class="fields" :class="classFields">
          <label for="">branches</label>
          <!-- TODO: should be filtered to be comma seperate format-->
          <div class="content">{{ branches }}</div>
          <Select class="content" v-model="branches"></Select>
        </div>
        <div class="fields" :class="classFields">
          <label for="">plugins</label>
          <!-- TODO: should be filtered to be formated json-->
          <div class="content">{{plugins}}</div>
          <Input class="content" v-model="plugins"></Input>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue, { PropType } from 'vue';

enum EnumMode{
  Edit='edit',
  View='view',
};

export default Vue.extend({
  name: 'New-Component',
  props: { 
    url: { type: String, default: '' },
    branches: { type: Array, default: () => [] },
  }, 
  components: {
  },
  data() {
    return {
      helloworold: 'helloworld' as string,
      operation: EnumMode.View as EnumMode,
    };
  },
  computed: {
    classFields() {
      return 'col-4';
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
</style>

