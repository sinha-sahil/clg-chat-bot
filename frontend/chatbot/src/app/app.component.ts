import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ApiService } from './Service/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  messages: any[];
  messageInput: FormGroup;
  constructor(private api: ApiService, private fb: FormBuilder){
    this.messages = [];
    this.messageInput = this.fb.group({
      messageText: ["", Validators.required]
    })
  }

  chat(){
    this.messages.push(
      { value: this.messageInput.value.messageText
      , sent: true
      }
      );
    this.api.chat(this.messageInput.value.messageText).subscribe(
      data => {
        this.messages.push({ value: data.response, sent:false});
        }
    );
    this.messageInput.reset();
    console.log(this.messages);
  }
}
