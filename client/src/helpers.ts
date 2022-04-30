import { testStore } from "./stores/test-store";

export const getTests = async () => {
	const res = await fetch('/api/test');
	const tests = await res.json();

	testStore.set({
		selectedTestIndex: 0,
		tests
	});
}
