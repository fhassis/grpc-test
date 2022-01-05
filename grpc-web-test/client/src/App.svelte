<script lang="ts">
	import { HelloRequest } from './autocode/helloworld_pb';
	import { GreeterClient } from './autocode/HelloworldServiceClientPb';

	const client = new GreeterClient('http://localhost:8080');

	let request = new HelloRequest();
	request.setName('Fabio');

	client.sayHello(request, {}, (err, response) => {
		console.log(response.getMessage());
	});
</script>

<h1>Hello World!</h1>
