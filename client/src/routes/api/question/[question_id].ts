import type { RequestHandler } from '@sveltejs/kit';

export const get: RequestHandler = async (event) => {
	const res = await fetch(
		`http://localhost:8080/question/${event.params.question_id}${event.url.search}`
	);
	const question = await res.json();

	return {
		body: question
	};
};
