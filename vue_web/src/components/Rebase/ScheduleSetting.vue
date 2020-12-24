<template>
  <div class="schedule-root">
    <div class="container">
      <div class="row control-pannel">
        <div class="col-12">
          <div class="d-flex justify-content-between">
            <Checkbox class="select-all" v-model="flagSelectAll" @on-change="handleSelectAll"> Select All</Checkbox>
            <i class="fas fa-plus" @click="handleAddNew" v-if="!flagAddNew" ></i>
            <i class="fas fa-trash-alt" @click="handleDelete"></i>
          </div>
        </div>
        <div class="col-12">
          <div class="row">
            <EditableRepositoryRecord
               :editMode="flagAddNew"
               v-if="flagAddNew"
               @save="handleSave"
               class="col"
               />
          </div>
        </div>
      </div>
      <div v-for="record of dataList" class="row">
        <Checkbox v-model="record.selected" @on-change="checkSelectAll"></Checkbox>
        <EditableRepositoryRecord
           class="col"
                                    :value="record"
                                    @save="handleSave"
                                    />
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue, { PropType } from 'vue';
import ScheduleService from '@/services/schedule';
import EditableRepositoryRecord from './components/editable-repository-record.vue';
import { RepositoryRecord } from '@/classes/apiModel/';

export default Vue.extend({
  name: 'New-Component',
  props: [],
  components: {
    EditableRepositoryRecord,
  },
  data() {
    return {
      dataList: [] as any[],
      flagAddNew: false as boolean,
      flagSelectAll: false as boolean,
    };
  },
  methods: {
    handleSelectAll(value: boolean) {
      this.dataList.forEach((record: RepositoryRecord) => { record.selected = this.flagSelectAll; });
    },
    checkSelectAll(value: boolean) {
      this.flagSelectAll = this.dataList.every((record: RepositoryRecord) => { return record.selected; })
    },
    async handleDelete() {
      const service = new ScheduleService();
      try {
        const requestList = this.dataList.map( async ( record: RepositoryRecord ) => {
          if ( record.selected) {
            this.response = await service.deleteTask(record.id);
          }
        });
        await Promise.all(requestList);
      }finally{
        this.get();
      }
    },
    handleAddNew() {
      this.flagAddNew = true;
    },
    async handleSave(record: RepositoryRecord) {
      const service = new ScheduleService();
      if(record.id){
        this.response = await service.updateTask(record.id, record);
      }else {
        this.response = await service.createTask(record);
      }
      await this.get();
    },
    async get() {
      let service = new ScheduleService();
      this.dataList = await service.getAllTask();
      this.flagAddNew = false;
    },
  },
  async created() {
    await this.get();
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

