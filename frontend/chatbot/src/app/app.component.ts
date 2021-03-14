import { Component } from '@angular/core';
import { ApiService } from './Service/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private api: ApiService){
    this.api.chat("hi").subscribe(
      data => console.log(data)
    )
  }

}
