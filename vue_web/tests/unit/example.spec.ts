import { shallowMount } from '@vue/test-utils';
import { RebaseSingleTask } from '@/components/Rebase';

jest.mock('@/services/rebase');
describe('RebaseSingleTask.vue', () => {
  it('happy path to check element created', () => {
    const wrapper = shallowMount(RebaseSingleTask, { });
    expect(wrapper.text()).toMatch('Single');
  });
  it('keyevent and check api calls', () => {
    const wrapper = shallowMount(RebaseSingleTask, { });
    wrapper.find('.task-root').trigger('keydown.shift.187');
    wrapper.find('.task-root').trigger('keydown.shift.187');
    wrapper.find('.task-root').trigger('keydown.shift.187');
    wrapper.find('.task-wrapper').trigger('keyup.enter');
  });
});
