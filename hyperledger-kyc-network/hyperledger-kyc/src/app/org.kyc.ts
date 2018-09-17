import {Asset} from './org.hyperledger.composer.system';
import {Participant} from './org.hyperledger.composer.system';
import {Transaction} from './org.hyperledger.composer.system';
import {Event} from './org.hyperledger.composer.system';
// export namespace org.kyc{
   export class UserData {
      name: string;
      encrypted_id: string;
      postcode: string;
      birthdate: string;
      merkle_root: string;
      rsa_public_key: string;
   }
   export class Administrator extends Participant {
      adminId: string;
   }
   export class User extends Participant {
      hashed_id: string;
      userData: UserData;
      access: boolean;
   }
   export class getUserData extends Transaction {
      user: User;
      userData: UserData;
   }
   export class createUser extends Transaction {
      hashed_id: string;
      userData: UserData;
      access: boolean;
   }
   export class deleteUser extends Transaction {
      hashed_id: string;
   }
   export class updateUserEncryptedData extends Transaction {
      hashed_id: string;
      newData: UserData;
   }
   export class grantAccess extends Transaction {
      hashed_id: string;
   }
   export class revokeAccess extends Transaction {
      hashed_id: string;
   }
   export class UserAccessRightsChanged extends Event {
      user: User;
      oldValue: boolean;
      newValue: boolean;
   }
   export class NewUserCreated extends Event {
      user: User;
   }
   export class UserDeleted extends Event {
      deleted_id: string;
   }
   export class UserEncryptedDataUpdated extends Event {
      user: User;
      oldName: string;
      oldEncryptedId: string;
      oldPostcode: string;
      oldBirthdate: string;
      oldMerkleRoot: string;
      oldRSAkey: string;
      newName: string;
      newEncryptedId: string;
      newPostcode: string;
      newBirthdate: string;
      newMerkleRoot: string;
      newRSAkey: string;
   }
// }
