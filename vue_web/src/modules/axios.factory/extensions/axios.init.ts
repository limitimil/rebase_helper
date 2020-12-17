import { AxiosRequestConfig } from 'axios';
/**
 * Intialize a http request
 * @param config - AXIOS request configuration
 */

export const httpInitRequest = (config: AxiosRequestConfig) => {

  // Base Url
  config.baseURL = connectionConfigs.VUE_APP_HOST_BACKEND_URL;

  // API Version
  if (config.params) {
    const apiVersion = config.params['api-version'];
    Object.assign(config.params, {
      'api-version': apiVersion ? apiVersion : 1,
    });
  } else {
    config.params = { 'api-version': 1 };
  }

  // Timeout
  config.timeout = IsTimeoutCustomized(config) ? config.timeout : HTTP_REQUEST_TIMEOUT;  // Milliseconds

  // Set header: content-type
  config.headers['Content-Type'] = 'application/json';

  // Set header: bearer token
  if (store.state.user && store.state.user.tokens) {
    const token = store.state.user.tokens.accessToken;
    config.headers.Authorization = `Bearer ${token}`;
  }
};


  /*
    AxiosRequestConfig default timeout is 0
    If timeout is not 0, that must be Customized
  */
const IsTimeoutCustomized = (requestConfig: AxiosRequestConfig) => {
  if (requestConfig.timeout === 0) {
    return false;
  }

  return true;
};

