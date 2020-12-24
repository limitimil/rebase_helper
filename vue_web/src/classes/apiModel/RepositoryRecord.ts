export default class RepositoryRecord{

  public id: string | null = null;
  public url: string;
  public repository_url: string[] = [];
  public plugins: any = {};
  constructor(fields?: any) {
    if (fields) {
        Object.assign(this, fields);
    }
  }
}


