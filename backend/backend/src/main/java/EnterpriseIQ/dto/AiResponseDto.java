package EnterpriseIQ.dto;

public class AiResponseDto {
   private String answer;

   public AiResponseDto(){}

   public AiResponseDto(String answer){
       this.answer=answer;
   }

   public void setAnswer(String answer){
       this.answer=answer;
   }
   public String getAnswer(){
       return answer;
   }

}