export type GetTestsResponse = {
	test_id: number;
	name: string;
	link: string;
}[];

export type PostTestsRequestBody = {
	name: string;
	link: string;
	data: [string[][]];
};

export type GetQuestionsResponse = {
	question_id: number;
	text: string;
}[];

export type GetQuestionResponse = {
	text: string;
	type: 'text' | 'variant' | 'number';
	stats?: Record<string | number, number>;
};
