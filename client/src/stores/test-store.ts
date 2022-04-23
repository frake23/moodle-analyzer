import { writable } from 'svelte/store';
import type { GetTestsResponse } from '../types';

interface TestStore {
	selectedTestIndex: number;
	tests?: GetTestsResponse;
}

export const testStore = writable<TestStore>({
	selectedTestIndex: 0
});
