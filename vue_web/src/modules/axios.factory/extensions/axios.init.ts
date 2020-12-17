import { AxiosRequestConfig } from 'axios';
/**
 * Intialize a http request
 * @param config - AXIOS request configuration
 */

export const httpInitRequest = (config: AxiosRequestConfig) => {

  config.baseURL = "http://192.168.107.135:9016";

};


