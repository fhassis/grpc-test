<script lang="ts">
	// import { GreeterClient } from "./autocode/greeter_grpc_web_pb";
	// import { HelloRequest } from "./autocode/greeter_pb";

	// var greeterClient = new GreeterClient("http://localhost:9091");

	// var request = new HelloRequest();
	// request.setName("Fabito");

	// greeterClient.sayHello(request, {}, (err, response) => {
	// 	if (err) {
	// 		console.log(err.code, err.message);
	// 	} else {
	// 		console.log(response.getMessage());
	// 	}
	// });

	import { onMount } from "svelte";
	import { GrpcWebFetchTransport } from "@protobuf-ts/grpcweb-transport";
	import { GreeterClient } from "./autocode/greeter.client";

	const transport = new GrpcWebFetchTransport({
		baseUrl: "http://127.0.0.1:8080",
		format: "text",
	});

	const greeter = new GreeterClient(transport);

	onMount(async () => {
		try {
			const { response } = await greeter.sayHello({ name: "Fabito" });
			console.log("response", response.message);
		} catch (error) {
			console.log("error", error);
		}

		try {
			const counterStream = greeter.counterStream({});
			for await (let response of counterStream.responses) {
				console.log("counter", response.counter);
			}
		} catch (error) {
			console.log("error", error);
		}
	});
</script>

<main>
	<h1>Hello gRPC-WEB</h1>
</main>

<style>
</style>
