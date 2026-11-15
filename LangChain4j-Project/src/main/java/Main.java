import dev.langchain4j.model.openai.OpenAiChatModel;

public class Main {
    public static void main(String[] args) {
        // 方式1：使用环境变量中的真实 API Key
        // String apiKey = System.getenv("OPENAI_API_KEY");
        // OpenAiChatModel model = OpenAiChatModel.builder()
        //         .apiKey(apiKey)
        //         .modelName("gpt-4o-mini")
        //         .build();

        // 方式2：使用文档提供的 demo 配置，无需自己的 Key，适合快速测试
        OpenAiChatModel model = OpenAiChatModel.builder()
                .baseUrl("http://langchain4j.dev/demo/openai/v1")
                .apiKey("demo")
                .modelName("gpt-4o-mini")
                .build();

        String answer = model.chat("Say 'Hello World'");
        System.out.println(answer); // 预期输出: Hello World
    }
}