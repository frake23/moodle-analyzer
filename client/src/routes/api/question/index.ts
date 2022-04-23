import type { RequestHandler } from '@sveltejs/kit';

export const get: RequestHandler = async (event) => {
	const data = event.request.url;
	console.log(data);
	const res = await fetch('http://localhost:8080/question');
	const questions = await res.json();

	return {
		body: questions
	};
};
