import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Home from '../views/Home.vue';
import { RebaseScheduleSetting, RebaseSingleTask } from '@/components/Rebase';

Vue.use(VueRouter);

const routes: RouteConfig[] = [
  {
    path: '/',
    name: 'Home',
    redirect: '/rebase',
  },
  {
    path: '/rebase',
    name: 'rebase_home',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: RebaseSingleTask,
  },
  {
    // TODO: router hierarchy should be adjust to make /rebase/schedule under /rebase
    path: '/rebase/schedule',
    name: 'rebase_schedule',
    component: RebaseScheduleSetting,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
