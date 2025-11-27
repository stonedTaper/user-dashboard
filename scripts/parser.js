import { parse } from 'csv-parse';
import { promisify } from 'util';

const parseAsync = promisify(parse);

export async function parseFile(filePath) {
  const file = await import('fs').then(({ promises: { readFile } }) => readFile(filePath, 'utf8'));
  const records = await parseAsync(file, { from: 'csv' });
  return records;
}