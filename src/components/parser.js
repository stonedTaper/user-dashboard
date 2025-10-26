// parser.js

import { parse } from 'csv-parser';

class Parser {
  constructor(file) {
    this.file = file;
    this.data = [];
    this.options = {
      delimiter: ',',
      header: true,
      skipLines: 1,
    };
  }

  async read() {
    return new Promise((resolve, reject) => {
      const data = [];
      const fileStream = this.file.read();
      fileStream.pipe(parse(this.options)).on('data', (row) => {
        data.push(row);
      }).on('end', () => {
        resolve(data);
      }).on('error', (err) => {
        reject(err);
      });
    });
  }
}

export { Parser };