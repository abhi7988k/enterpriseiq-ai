package EnterpriseIQ.controller;


import EnterpriseIQ.dto.AiRequestDto;
import EnterpriseIQ.dto.AiResponseDto;
import EnterpriseIQ.service.AiService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/ai")
public class AiController {

    private final AiService aiService;

    public AiController(AiService aiService){
        this.aiService=aiService;
    }
    @PostMapping("/chat")
    public AiResponseDto chat(@RequestBody AiRequestDto request){
        return  aiService.chat(request);
    }
}
