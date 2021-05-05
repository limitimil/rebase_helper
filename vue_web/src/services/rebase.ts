import { AxiosResponse } from 'axios';
import axios from '@/modules/axios.factory';

export default class Rebase {
  public async executeSingleTaskAsync(payload: any): Promise<any> {
    const url = 'api/rebase/execute';
    const res: AxiosResponse<any> = await axios.post(url, payload);
    return res.data;
  }
}

