import assert from 'node:assert/strict';
import test from 'node:test';
import { requiredStock } from './inventory.ts';

test('required stock returns a successful zero with one read', async () => {
  let calls = 0;
  assert.equal(await requiredStock(async () => { calls++; return 0; }), 0);
  assert.equal(calls, 1);
});

test('required stock propagates the original read error with no retry', async () => {
  const failure = new Error('Stock service unavailable');
  let calls = 0;
  await assert.rejects(requiredStock(async () => { calls++; throw failure; }), (error) => error === failure);
  assert.equal(calls, 1);
});
