package EnterpriseIQ.service;

import EnterpriseIQ.dto.AiRequestDto;
import EnterpriseIQ.dto.AiResponseDto;
import org.springframework.stereotype.Service;
import tools.jackson.databind.ObjectMapper;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;

@Service
public class AiService {

    private final ObjectMapper objectMapper;

    public AiService(ObjectMapper objectMapper) {
        this.objectMapper = objectMapper;
    }

    public AiResponseDto chat(AiRequestDto request) {

        try {
            String json = objectMapper.writeValueAsString(request);

            System.out.println("JSON SENT: " + json);

            HttpClient client = HttpClient.newBuilder()
                    .version(HttpClient.Version.HTTP_1_1)
                    .build();

            HttpRequest httpRequest = HttpRequest.newBuilder()
                    .uri(URI.create(
                            "http://127.0.0.1:8000/api/ai/chat"
                    ))
                    .version(HttpClient.Version.HTTP_1_1)
                    .header("Content-Type", "application/json")
                    .header("Accept", "application/json")
                    .POST(
                            HttpRequest.BodyPublishers.ofByteArray(
                                    json.getBytes(StandardCharsets.UTF_8)
                            )
                    )
                    .build();

            HttpResponse<String> response = client.send(
                    httpRequest,
                    HttpResponse.BodyHandlers.ofString()
            );

            System.out.println(
                    "FastAPI STATUS: " + response.statusCode()
            );

            System.out.println(
                    "FastAPI RESPONSE: " + response.body()
            );

            if (response.statusCode() < 200
                    || response.statusCode() >= 300) {
                throw new RuntimeException(
                        "FastAPI returned status "
                                + response.statusCode()
                                + ": " + response.body()
                );
            }

            return objectMapper.readValue(
                    response.body(),
                    AiResponseDto.class
            );

        } catch (Exception e) {
            throw new RuntimeException(
                    "Failed to call AI service", e
            );
        }
    }
}
