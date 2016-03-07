def app(env, start_response):
	status = '200 OK'
	response_headers = [('Content-Type', 'text/plain')]
	start_response(status, response_headers)
	response = env['QUERY_STRING'].split("&")
	response = [item+"\r\n" for item in response]
	return response