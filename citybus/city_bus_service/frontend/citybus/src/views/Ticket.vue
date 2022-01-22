<template >
    <div class="row">
        <div class="container">
            <div class="row mt-4 mb-2 text-center">
                <h3 class="display-5">Your purchased ticket history</h3>
            </div>

        </div>
        

    </div>
    <div class="row">
        <div class="container">
            <div class="row">
                <div class="center">
                
                <button @click="review()" class="btn btn-dark">Please tell us about your journey 🗣</button>
                <br>
                
            </div>
            
        </div>

        </div>
    </div>
    <div class="row">
        <div class="container">
            <div v-if='show' class="my-3">
                <div class="container">
                    <div class="form-group">
                 <label for="exampleFormControlTextarea1">Submit your review</label>
                <textarea v-model='message' class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                
                <button v-if='button === false' @click="submit()" class="btn btn-primary mt-2">Submit</button>
                <button v-if='button' class="btn btn-primary" type="button" disabled>
                    <span
                        class="spinner-border spinner-border-sm"
                        role="status"
                        aria-hidden="true"
                    ></span>
                     Submitting...
                </button>
                
            </div>

                </div>
            
        </div>
        </div>
    </div>
    <div class="row">
            <div class="text-center my-3">
                <div v-if='thankyou' class="display-5"><b>Thank you!! for your valuable reply 😻</b></div>
            </div>

        </div>
        

    
    <div v-if='ticketNull' class="contianer">
        <h1 class="display-5 text-center mt-5">There is no ticket yet 🤷</h1>
    </div>
    

    <div  v-else class="container">   
        
            
            




            
            <table class="table mx-2 mt-3 mb-5">
                
            <thead>
                <tr>
                <th scope="col">Bus name</th>
                <th scope="col">Pickup point</th>
                <th scope="col">Destination</th>
                <th scope="col">Time</th>
                <th scope="col">Cancel</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="ticket in ticket_obj" :key="ticket.id">
                    <th>
                        <span class="mt-2 mx-2">
                            <i class="fas fa-bus-alt"></i>
                        </span>
                        <b>{{ticket.busname}}</b>
                    </th>
                    <th>{{ticket.pickup}}</th>
                    <th>{{ticket.destination}}</th>
                    <th>{{ticket.time}}</th>
                    <th>
                        <button @click="cancel(ticket.id,ticket.time)" class="btn btn-primary">Cancel</button>
                    </th>
                </tr>
                
            </tbody>
            </table>
            
            
        </div>
        
        
        <router-view></router-view>
        
   
</template>
<script>
import axios from 'axios'
export default {

    data(){
        return{
            ticket_obj:[],
            show:false,
            message:'',
            thankyou:false,
            button:false,
            blank:false,
            tickeNull:false,
        }
    },

    async created() {
        console.log(this.ticket_obj)
        const id = this.$store.state.user.id
        await axios.get(`api/single_ticket/${id}`)
        .then(res => {
            console.log(res.data)
            if(res.data['data'] !== 'There is no ticket yet'){
                this.ticket_obj = res.data['data']

            }
            else{
                this.ticket_obj = []
                this.tickeNull = true
            }
            
        })
    },
    methods:{
        async cancel(id,time){
            console.log(id,time)
            //console.log(this.ticket_obj)
            const data = {
                id:id,
                time:time
            }
            //console.log(data['id'])
            await axios.put('/api/ticket/',data)
            .then(res => {
                console.log(res)
                this.ticket_obj = this.ticket_obj.filter((ticket) => ticket.id !==id)
                console.log(this.ticket_obj.length)
                if(this.ticket_obj.length === 0){
                    this.tickeNull = true
                }
                // const id = this.$store.state.user.id
                // axios.get(`api/single_ticket/${id}`)
                // .then(res => {
                //     if(res.data['data'] !== 'There is no ticket yet'){

                //         this.ticket_obj = res.data['data']

                //     }
                //     else{
                //         this.blank = true
                //     }
                    

                // })
                
            })
            //console.log(data)
        },
        review(){
            this.show = !this.show
        },
        async submit(){
            this.button = true
            const data = {
                user:this.$store.state.user.id,
                review: this.message
            }
            await axios.post('api/review_post/',data)
            .then(res => {
                console.log(res)
                this.thankyou = true
                this.show = false 
                this.button = false
            })
            .then(err => {
                console.log(err)
            })
        }
    }
}
</script>
<style >
 
</style>