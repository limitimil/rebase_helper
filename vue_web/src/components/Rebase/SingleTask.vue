<template>
  <div v-on:keydown.shift.187.prevent="newSlot">
    <h1>Rebase: {{mode}} Task</h1>
    <p>press 'enter' to start</p>
    <p>press '+' to create new slot</p>
    <div class="hack1">{{payloads}}</div>
    <div class="container-fluid" v-on:keyup.enter="start">
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
import axiosFactory from '@/modules/axios.factory';

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
      helloworold: 'helloworld' as string,
      axios: axiosFactory() as any,
    };
  },
  computed: {
    mode(): string{
      return this.payloads.length > 1 ? 'Multiple': 'Single';
    }
  },
  methods: {
    newSlot() {
      const newObj = {};
      Object.assign(newObj, this.payloads[this.payloads.length -1 ])
      this.payloads.push(newObj);
    },
    async start() {
      // TODO: api calls should extract to another module
      // TODO: should handler not 200 response
      const path = '/api/rebase/execute';
      try {
        this.$Loading.start();
        await this.axios.post(path, this.payloads[0]);
        this.$Loading.finish();
      } catch (err) {
        this.$Loading.error();
      }
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

