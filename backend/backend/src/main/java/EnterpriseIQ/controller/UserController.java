package EnterpriseIQ.controller;


import EnterpriseIQ.dto.RegisterRequestDto;


import EnterpriseIQ.dto.UserResponseDto;
import EnterpriseIQ.entity.User;
import EnterpriseIQ.service.UserService;
import jakarta.validation.Valid;

import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/users")
public class UserController {

    private final UserService userService;
    public UserController(UserService userService){
        this.userService=userService;
    }

    @PostMapping
    public UserResponseDto createUser(@Valid  @RequestBody RegisterRequestDto request){
        return  userService.createUser(request);
    }

    @GetMapping("/profile")
    public UserResponseDto getProfile(Authentication authentication){
        User user=(User) authentication.getPrincipal();
        return  new UserResponseDto(
                user.getId(),
                user.getName(),
                user.getEmail(),
                user.getRole()
        );
    }

    @GetMapping("/{id}")
    public UserResponseDto getUserById(@PathVariable Long id){
        return userService.getUserById(id);
    }
}
