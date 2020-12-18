<template>
  <div v-on:keydown.shift.187.prevent="newSlot" class="task-root">
    <h1>Rebase: {{mode}} Task</h1>
    <p>press 'enter' to start</p>
    <p>press '+' to create new slot</p>
    <div class="hack1">{{payloads}}</div>
    <div class="container-fluid task-wrapper" v-on:keyup.enter="start" :class="currentStatus">
      <div v-for="p in payloads" class="row" style="padding-top: 1em">
        <label class="col-lg-3 col-md-6" for="">Repository Url:</label>
        <Input class="col-lg-3 col-md-6" v-model="p.url"></Input>
        <label class="col-lg-3 col-md-6" for="">Branch Name:</label>
        <Input class="col-lg-3 col-md-6" v-model="p.branch"></Input>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue, { PropType } from 'vue';
import RebaseService from '@/services/rebase';
enum EnumCurrentStatus{
  WaitInput= 'wait-input',
  InProgress= 'in-progress',
};
export default Vue.extend({
  name: 'New-Component',
  props: [],
  components: {
  },
  data() {
    return {
      payloads: [{
        url: "",
        branch: "",
      }] as any[],
      currentStatus: EnumCurrentStatus.WaitInput,
      EnumCurrentStatus
    };
  },
  computed: {
    mode(): string{
      return this.payloads.length > 1 ? 'Multiple': 'Single';
    }
  },
  methods: {
    initiPayloads(){
      this.payloads = [{
        url: "",
        branch: "",
      }];
    },
    newSlot() {
      const newObj = {};
      Object.assign(newObj, this.payloads[this.payloads.length -1 ])
      this.payloads.push(newObj);
    },
    async start() {
      // TODO: api calls should extract to another module
      // TODO: should handler not 200 response
      try {
        this.$Loading.start();
        this.currentStatus = EnumCurrentStatus.InProgress;
        const service = new RebaseService();
        while(this.payloads.length){
          await service.executeSingleTaskAsync(this.payloads[0]);
          this.payloads.shift();
        }
        this.$Loading.finish();
        this.currentStatus = EnumCurrentStatus.WaitInput;
      } catch (err) {
        this.$Loading.error();
        this.currentStatus = EnumCurrentStatus.WaitInput;
      }
    },
  },
});
</script>
<style scoped lang="less">
  // hack
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
  // feature

.in-progress > .row:first-child {
  background-color: yellow;
}
</style>

