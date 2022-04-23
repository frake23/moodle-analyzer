export async function get() {
	const res = await fetch('http://localhost:8080/question');
	const tests = await res.json();

	return {
		body: tests
	};
}
