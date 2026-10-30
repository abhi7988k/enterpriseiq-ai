package EnterpriseIQ.service;


import EnterpriseIQ.dto.LoginRequestDto;
import EnterpriseIQ.dto.LoginResponseDto;
import EnterpriseIQ.entity.User;
import EnterpriseIQ.exception.InvalidCredentialsException;
import EnterpriseIQ.repository.UserRepository;
import EnterpriseIQ.security.JwtService;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class AuthService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtService jwtService;

    public AuthService(UserRepository userRepository,PasswordEncoder passwordEncoder,JwtService jwtService){
        this.userRepository=userRepository;
        this.passwordEncoder=passwordEncoder;
        this.jwtService=jwtService;
    }

    public LoginResponseDto login(LoginRequestDto requestDto){
        User user=userRepository
                .findByEmail(requestDto.getEmail())
                .orElseThrow(() ->new InvalidCredentialsException("Invalid email or password"));

        boolean passwordMatcher=passwordEncoder.matches(requestDto.getPassword(),user.getPassword());
        if(!passwordMatcher){
            throw new InvalidCredentialsException("Invalid email or password");
        }

        String token=jwtService.generateToken(user);
        return  new LoginResponseDto(
                user.getId(),
                user.getName(),
                user.getEmail(),
                user.getRole(),
                token
        );

    }
}
