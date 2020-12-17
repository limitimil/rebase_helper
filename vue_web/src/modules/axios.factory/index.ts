import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';
import { httpInitRequest } from '@/modules/axios.factory/extensions';

axios.interceptors.request.use(
  (config: AxiosRequestConfig) => {

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
    // TODO: define a general request fail handling behavior.
      return Promise.reject(error);
  },
);

export default axios;
