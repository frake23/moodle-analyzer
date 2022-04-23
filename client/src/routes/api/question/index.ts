import type { RequestHandler } from '@sveltejs/kit';

export const get: RequestHandler = async (event) => {
	const res = await fetch(`http://localhost:8080/question${event.url.search}`);
	const questions = await res.json();

	return {
		body: questions
	};
};
