import { shallowMount } from '@vue/test-utils';
import { RebaseSingleTask } from '@/components/Rebase';

describe('RebaseSingleTask.vue', () => {
  it('renders props.msg when passed', () => {
    const wrapper = shallowMount(RebaseSingleTask, { });
    expect(wrapper.text()).toMatch('Single');
  });
});
