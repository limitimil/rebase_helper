import { AxiosResponse } from 'axios';
import axios from '@/modules/axios.factory';

export default class NewService {
  public topic = 'schedule'
  private getUrl(): string {
    return `api/${this.topic}`
  }
  public async getAsync(): Promise<any> {
    const url = this.getUrl();
    const res: AxiosResponse<any> = await axios.get(url);
    return res.data;
  }
  public async putAsync(): Promise<any> {
    const url = this.getUrl();
    const res: AxiosResponse<any> = await axios.put(url);
    return res.data;
  }
  public async postAsync(): Promise<any> {
    const url = this.getUrl();
    const res: AxiosResponse<any> = await axios.post(url);
    return res.data;
  }
  public async deleteAsync(): Promise<any> {
    const url = this.getUrl();
    const res: AxiosResponse<any> = await axios.delete(url);
    return res.data;
  }
}

