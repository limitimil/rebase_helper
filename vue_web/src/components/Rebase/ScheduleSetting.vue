<template>
  <div class="schedule-root">
    <div class="hack2">
      <div class="poc-hint hack1">{{response}}</div>
      <Button class="hack1" @click="get">get</Button>
      <Button class="hack1" @click="post">post</Button>
      <Button class="hack1" @click="delete2">delete</Button>
      <Input v-model="docId" placeholder="docuemnt id"></Input>
      <Input v-model="content" placeholder="content"></Input>
    </div>
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
      response: '' as string,
      docId: '' as string,
      content: `[
        {
                'repository_url':'http://tfs.cybersoft4u.com.tw:8080/tfs/SDD/TIS/_git/CloudTisTesting',
                'branches': [
                    'tool-CTIS-xxxx',
                    'tool-CTIS-2149',
                    ],
                'plugin_actions': {
                        'python-lint':{
                                'name': 'python-lint',
                                'targets': ['testtools', 'testutils', 'unittests'],
                        }
                }
        },
]`as string,
    };
  },
  methods: {
    async get() {
      let service = new ScheduleService();
      this.response = await service.getAllTask();
    },
    async post() {
      let service = new ScheduleService();
      const content = JSON.parse(this.content);
      if(this.docId){
        this.response = await service.updateTask(this.docId, content);
      }else {
        this.response = await service.createTask(content);
      }
    },
    async delete2() {
      let service = new ScheduleService();
      this.response = await service.deleteTask(this.docId);
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

