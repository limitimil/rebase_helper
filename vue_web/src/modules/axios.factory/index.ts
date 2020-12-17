import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';
import { httpInitRequest } from '@/modules/axios.factory/extensions';

axios.interceptors.request.use(
  (config: AxiosRequestConfig) => {

    const routeName: string | undefined = router.currentRoute.name;

    // Initialize the http request
    httpInitRequest(config);

    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);

axios.interceptors.response.use(
  (response: AxiosResponse<any>) => {

    return response;
  },
  async (error: any) => {
      return Promise.reject(error);
  },
);

export default axios;
