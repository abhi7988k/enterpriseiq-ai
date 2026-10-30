package EnterpriseIQ.service;





import EnterpriseIQ.dto.RegisterRequestDto;
import EnterpriseIQ.dto.UserResponseDto;
import EnterpriseIQ.entity.User;
import EnterpriseIQ.exception.EmailAlreadyExistsException;
import EnterpriseIQ.repository.UserRepository;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public UserService(UserRepository userRepository,PasswordEncoder passwordEncoder){
        this.userRepository=userRepository;
        this.passwordEncoder=passwordEncoder;
    }

    public UserResponseDto createUser(RegisterRequestDto request){
        User user=new User();

        if (userRepository.existsByEmail(request.getEmail())) {
            throw new EmailAlreadyExistsException("Email all ready exists");
        }
        user.setName(request.getName());
        user.setEmail(request.getEmail());

        String encodedPassword=passwordEncoder.encode(request.getPassword());
        user.setPassword(encodedPassword);
        user.setRole("USER");

        User savedUser=userRepository.save(user);

        return new UserResponseDto(
                savedUser.getId(),
                savedUser.getName(),
                savedUser.getEmail(),
                savedUser.getRole()
        );

    }

    public UserResponseDto getUserById(Long id){
        User user=userRepository.findById(id).orElseThrow(()-> new RuntimeException("user not found"));
        return  new UserResponseDto(
                user.getId(),
                user.getName(),
                user.getEmail(),
                user.getRole()
        );
    }
}
