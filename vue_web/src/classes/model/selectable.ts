export default class Selectable  {

  public selected: boolean = false;
  constructor(fields?: any) {
    if (fields) {
        Object.assign(this, fields);
    }
  }
}


