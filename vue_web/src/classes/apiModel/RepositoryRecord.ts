import { Selectable } from '@/classes/model/';

export default class RepositoryRecord extends Selectable{

  public id: string | null = null;
  public repository_url: string;
  public branches: string[] = [];
  public plugins: any = {};
  constructor(fields?: any) {
    super(fields);
    if (fields) {
        Object.assign(this, fields);
    }
  }
}


