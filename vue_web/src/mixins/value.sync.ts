import Vue from 'vue';

export default Vue.extend({
  watch: {
    value(newValue: any, oldValue: any) {
      const vm: any = this;
      vm.$emit('update:value', newValue);
      vm.$emit('on-change', newValue);
    },
  },
  methods: {
    emitTouched() {
      const vm: any = this;
      vm.$emit('on-touched');
    },
  },
});


