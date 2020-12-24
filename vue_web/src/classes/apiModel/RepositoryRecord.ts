export default class RepositoryRecord{

  public id: string | null = null;
  public repository_url: string;
  public branches: string[] = [];
  public plugins: any = {};
  constructor(fields?: any) {
    if (fields) {
        Object.assign(this, fields);
    }
  }
}


