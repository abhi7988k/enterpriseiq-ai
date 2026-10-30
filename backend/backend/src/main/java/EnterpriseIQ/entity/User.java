package EnterpriseIQ.entity;

import jakarta.persistence.*;


@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="user_id")
    private  Long id;

    @Column(name = "name")
    private  String name;

    @Column(name = "email" , unique = true,nullable = false)
    private String email;

    @Column(name = "password" ,nullable = false)
    private  String password;

    @Column(name = "role")
    private String role;


    public  User(){}

    public User(String name, String email, String password, String role){
        this.name=name;
        this.email=email;
        this.password=password;
        this.role=role;
    }

    //Getter and Setter

    public void setId(Long id){
        this.id=id;
    }
    public  void setName(String name){
        this.name=name;
    }
    public  void setEmail(String email){
        this.email=email;
    }
    public  void setPassword(String password){
        this.password=password;
    }
    public  void setRole(String role){
        this.role=role;
    }

    public Long getId(){
        return  id;
    }

    public String getName(){
        return name;
    }

    public String getEmail(){
        return  email;
    }
    public String getPassword(){
        return  password;
    }
    public String getRole(){
        return  role;
    }
}
