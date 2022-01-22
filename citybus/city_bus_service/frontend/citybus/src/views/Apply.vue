<template>
    <div>
        <div class="container">
        <div class="card" style="width: 40rem;">
        <div class="card-header my-2">
            <h3>Are you freedom fighter, student or disabled?</h3>
            <b>We offer you 50% off ❤️</b>
            <br>
            <small class="muted">Please submit your file for verification [ Ex: Freedom fighter certificate, Academic transcript etc ]</small>
        </div>
        <div class="card-body">
            

                <div v-if='message_box===true' class="my-2 text-center">
                    <h1>Thank You !!</h1>
                    <p class="muted">We will inform you very soon, Please stay with us.
                        <router-link to='/'>Back to home page</router-link>

                    </p>
                </div>

                <div v-if="message_box === false">
                    <div class="mb-3">
                    <label class="form-label" for="customFile">Upload your credential</label>
                    <input type="file" v-on:change="handlefile( $event )" class="form-control" id="customFile" required/>
                    
                </div>
                <div class="mb-3">
                    <label class="form-label" for="exampleFormControlTextarea1">Want to say something?</label>
                    <textarea v-model='message' class="form-control my-2" id="exampleFormControlTextarea1" rows="3"></textarea>
                </div>
                
                

                <button type="submit" @click="submit()" class="btn btn-primary">Submit</button>

                

                </div>
            
                
           
            
        </div>
    </div>
    
    </div>
    <router-view></router-view>

    </div>
    
    
</template>

<script>
import axios from 'axios'
export default {
    name:'Apply',
    data(){
        return{
            file:null,
            message:'',
            message_box:false,
            
        }
    },
    methods:{
        handlefile(event){
        console.log(event.target.files[0])
        this.file = event.target.files[0]
      },
      submit(){
          const formData = new FormData();
            /*
                Add the form data we need to submit
            */
            formData.append('file', this.file,this.file.name);
            formData.append('message',this.message)
            formData.append('user',this.$store.state.user.id)
            if(this.file === null){
                this.upload_file_null = true
            }
            axios.post('api/apply_half/',formData)
            .then(res => {
                console.log(res)
                this.message_box = true
                
            })
            .then(err => {
                console.log(err)
            })
      }
    }
}
</script>

<style scoped>
.container{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    
}
.card{
    margin-top: 3rem;
} 
h2{
    font-weight: 900;
}

</style>>

