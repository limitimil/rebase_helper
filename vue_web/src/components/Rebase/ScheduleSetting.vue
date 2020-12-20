<template>
  <div class="schedule-root">
    <div class="poc-hint">{{response}}</div>
    <Button class="poc" @click="get">get</Button>
    <Button class="poc" @click="put">put</Button>
    <Button class="poc" @click="post">post</Button>
    <Button class="poc" @click="delete2">delete</Button>
  </div>
</template>
<script lang="ts">
import Vue, { PropType } from 'vue';
import ScheduleService from '@/services/schedule';

export default Vue.extend({
  name: 'New-Component',
  props: [],
  components: {
  },
  data() {
    return {
      response: '' as string
    };
  },
  methods: {
    async get() {
      let service = new ScheduleService();
      this.response = await service.getAsync();
    },
    async put() {
      let service = new ScheduleService();
      this.response = await service.putAsync();
    },
    async post() {
      let service = new ScheduleService();
      this.response = await service.postAsync();
    },
    async delete2() {
      let service = new ScheduleService();
      this.response = await service.deleteAsync();
    },
  }
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

