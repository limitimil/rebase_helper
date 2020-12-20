import { AxiosResponse } from 'axios';
import axios from '@/modules/axios.factory';

export default class NewService {
  public topic = 'schedule'
  public async getAllTask(): Promise<any> {
    const url = `api/${this.topic}/all_task`;
    const res: AxiosResponse<any> = await axios.get(url);
    return res.data;
  }
  public async createTask(payload): Promise<any> {
    const url = `api/${this.topic}/task` ;
    const res: AxiosResponse<any> = await axios.post(url, payload);
    return res.data;
  }
  public async updateTask(taskId, payload): Promise<any> {
    const url = `api/${this.topic}/task/${taskId}`;
    const res: AxiosResponse<any> = await axios.post(url, payload);
    return res.data;
  }
  public async deleteTask(taskId): Promise<any> {
    const url = `api/${this.topic}/task/${taskId}`;
    const res: AxiosResponse<any> = await axios.delete(url);
    return res.data;
  }
}

