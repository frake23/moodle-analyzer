import type { RequestHandler } from '@sveltejs/kit';

export const get: RequestHandler = async () => {
	const res = await fetch(`${import.meta.env.VITE_HOST}/test`);
	const tests = await res.json();

	return {
		body: tests
	};
};

export const post: RequestHandler = async (event) => {
	const res = await fetch(`${import.meta.env.VITE_HOST}/test`, {
		method: 'POST',
		body: await event.request.text(),
		headers: { 'content-type': 'application/json' }
	});

	return {
		body: await res.json()
	};
};
