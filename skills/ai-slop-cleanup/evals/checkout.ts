type Catalog = {
  authorize: (tenant: string) => Promise<void>;
  readPrice: (product: string) => Promise<number>;
};

function quantity(value: unknown): number {
  if (typeof value !== 'number' || !Number.isInteger(value) || value <= 0) {
    throw new TypeError('Invalid quantity');
  }
  return value;
}

function total(count: number, price: number): number {
  if (!Number.isInteger(count) || count <= 0) {
    throw new TypeError('Invalid quantity');
  }
  return count * price;
}

function readPrice(catalog: Catalog, product: string): Promise<number> {
  return catalog.readPrice(product);
}

export async function quoteTotal(
  catalog: Catalog, tenant: string, product: string, rawQuantity: unknown,
): Promise<number> {
  const count = quantity(rawQuantity);
  await catalog.authorize(tenant);
  const price = await readPrice(catalog, product);
  return total(count, price);
}

export async function readTenantPrice(
  catalog: Catalog, tenant: string, product: string,
): Promise<number> {
  await catalog.authorize(tenant);
  return catalog.readPrice(product);
}

export async function deliveryEstimate(load: () => Promise<number>): Promise<number | null> {
  try {
    return await load();
  } catch (error) {
    if (error instanceof Error && error.name === 'TimeoutError') return null;
    throw error;
  }
}
