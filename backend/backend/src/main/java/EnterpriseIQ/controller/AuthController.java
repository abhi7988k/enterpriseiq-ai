package EnterpriseIQ.controller;


import EnterpriseIQ.dto.LoginRequestDto;
import EnterpriseIQ.dto.LoginResponseDto;
import EnterpriseIQ.entity.User;
import EnterpriseIQ.service.AuthService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/auth")
public class AuthController {

    private final AuthService authService;
    public  AuthController(AuthService authService){
        this.authService=authService;
    }

    @PostMapping("/login")
    public LoginResponseDto login(@RequestBody LoginRequestDto requestDto){
        return authService.login(requestDto);
    }
}
