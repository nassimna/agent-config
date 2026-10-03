export async function requiredStock(load: () => Promise<number>): Promise<number> {
  try {
    return await load();
  } catch {
    return 0;
  }
}
