import assert from 'node:assert/strict';
import test from 'node:test';
import { deliveryEstimate, quoteTotal, readTenantPrice } from './checkout.ts';

test('public paths return their values after one authorization and one price read', async () => {
  const events: string[] = [];
  const catalog = {
    authorize: async (tenant: string) => { events.push(`authorize:${tenant}`); },
    readPrice: async (product: string) => { events.push(`read:${product}`); return 12; },
  };
  assert.equal(await quoteTotal(catalog, 'shop', 'shirt', 3), 36);
  assert.deepEqual(events, ['authorize:shop', 'read:shirt']);
  events.length = 0;
  assert.equal(await readTenantPrice(catalog, 'shop', 'shirt'), 12);
  assert.deepEqual(events, ['authorize:shop', 'read:shirt']);
});

test('invalid runtime quantities are rejected before external calls', async () => {
  const events: string[] = [];
  const catalog = {
    authorize: async () => { events.push('authorize'); },
    readPrice: async () => { events.push('read'); return 12; },
  };
  for (const value of ['3', 0]) {
    await assert.rejects(quoteTotal(catalog, 'shop', 'shirt', value), TypeError);
  }
  assert.deepEqual(events, []);
});

test('both public price paths preserve denial and never read the price', async () => {
  const denied = new Error('Tenant denied');
  for (const invoke of [
    (catalog: Parameters<typeof quoteTotal>[0]) => quoteTotal(catalog, 'shop', 'shirt', 1),
    (catalog: Parameters<typeof quoteTotal>[0]) => readTenantPrice(catalog, 'shop', 'shirt'),
  ]) {
    const events: string[] = [];
    const catalog = {
      authorize: async () => { events.push('authorize'); throw denied; },
      readPrice: async () => { events.push('read'); return 12; },
    };
    await assert.rejects(invoke(catalog), (error) => error === denied);
    assert.deepEqual(events, ['authorize']);
  }
});

test('both public price paths preserve read errors and call ordering', async () => {
  const failure = new Error('Catalog unavailable');
  for (const invoke of [
    (catalog: Parameters<typeof quoteTotal>[0]) => quoteTotal(catalog, 'shop', 'shirt', 1),
    (catalog: Parameters<typeof quoteTotal>[0]) => readTenantPrice(catalog, 'shop', 'shirt'),
  ]) {
    const events: string[] = [];
    const catalog = {
      authorize: async () => { events.push('authorize'); },
      readPrice: async () => { events.push('read'); throw failure; },
    };
    await assert.rejects(invoke(catalog), (error) => error === failure);
    assert.deepEqual(events, ['authorize', 'read']);
  }
});

test('delivery estimate returns its result with one call', async () => {
  let calls = 0;
  assert.equal(await deliveryEstimate(async () => { calls++; return 8; }), 8);
  assert.equal(calls, 1);
});

test('optional delivery timeout returns null with no retry', async () => {
  const timeout = new Error('Timed out');
  timeout.name = 'TimeoutError';
  let calls = 0;
  assert.equal(await deliveryEstimate(async () => { calls++; throw timeout; }), null);
  assert.equal(calls, 1);
});

test('other delivery errors propagate unchanged', async () => {
  const failure = new Error('Delivery denied');
  let calls = 0;
  await assert.rejects(deliveryEstimate(async () => { calls++; throw failure; }), (error) => error === failure);
  assert.equal(calls, 1);
});
