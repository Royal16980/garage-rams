# Supabase Setup Guide for Garage RAMS App

## 🎯 What You Need

Your Garage RAMS app is now configured to connect to your Supabase project with these credentials:

- **Project URL**: `https://fylnmwkjqxvneiurnqqa.supabase.co`
- **Anonymous Key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ5bG5td2preHF2bmVpdXJucXFhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTU5NzgzOTAsImV4cCI6MjA3MTU1NDM5MH0.LGgd6ysDf8RFZHVjErGUG3lLqrPLDyd_7rBAe3jnMUo`
- **Service Role Key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ5bG5td2preHF2bmVpdXJucXFhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NTk3ODM5MCwiZXhwIjoyMDcxNTU0MzkwfQ.1xhPXtkI1tKOdde1uBGkoYyd1kXrfioI9q_wMg7fY6I`

## 🚀 Getting Started

### 1. **Test Your Connection**

Open your browser's developer console (F12) and run:

```javascript
// Test basic connection
window.testSupabase.testConnection();

// Test authentication
window.testSupabase.testAuth();

// Test database operations
window.testSupabase.testDatabase();

// Run all tests at once
window.testSupabase.runAllTests();
```

### 2. **Create Your Database Tables**

You'll need to create these tables in your Supabase dashboard:

#### **assessments** table
```sql
CREATE TABLE assessments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task TEXT NOT NULL,
  description TEXT,
  severity INTEGER CHECK (severity >= 1 AND severity <= 5),
  likelihood INTEGER CHECK (likelihood >= 1 AND likelihood <= 5),
  risk_score INTEGER GENERATED ALWAYS AS (severity * likelihood) STORED,
  risk_level TEXT GENERATED ALWAYS AS (
    CASE 
      WHEN severity * likelihood <= 4 THEN 'LOW'
      WHEN severity * likelihood <= 8 THEN 'MEDIUM'
      ELSE 'HIGH'
    END
  ) STORED,
  control_measures TEXT[],
  responsible_person TEXT,
  review_date DATE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  user_id UUID REFERENCES auth.users(id),
  company_id UUID
);
```

#### **users** table
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY REFERENCES auth.users(id),
  email TEXT UNIQUE NOT NULL,
  full_name TEXT,
  role TEXT DEFAULT 'technician' CHECK (role IN ('admin', 'manager', 'supervisor', 'technician', 'viewer')),
  company_id UUID,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### **teams** table
```sql
CREATE TABLE teams (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  description TEXT,
  company_id UUID,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### **team_members** table
```sql
CREATE TABLE team_members (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  team_id UUID REFERENCES teams(id) ON DELETE CASCADE,
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  role TEXT DEFAULT 'member' CHECK (role IN ('admin', 'manager', 'member')),
  joined_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  UNIQUE(team_id, user_id)
);
```

### 3. **Enable Row Level Security (RLS)**

Enable RLS on all tables and create policies:

```sql
-- Enable RLS
ALTER TABLE assessments ENABLE ROW LEVEL SECURITY;
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE teams ENABLE ROW LEVEL SECURITY;
ALTER TABLE team_members ENABLE ROW LEVEL SECURITY;

-- Create policies
CREATE POLICY "Users can view their own assessments" ON assessments
  FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can create their own assessments" ON assessments
  FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own assessments" ON assessments
  FOR UPDATE USING (auth.uid() = user_id);

CREATE POLICY "Users can view their own profile" ON users
  FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update their own profile" ON users
  FOR UPDATE USING (auth.uid() = id);
```

## 🔧 Configuration Files

### **Main Config**: `src/config/supabase.js`
This is where you can update your Supabase credentials if they change.

### **Auth System**: `src/lib/auth.js`
Handles user authentication, 2FA, and role-based access control.

### **Cloud Sync**: `src/lib/cloud.js`
Manages data synchronization between local storage and Supabase.

### **API Integration**: `src/lib/api.js`
Provides RESTful API endpoints for external integrations.

## 🧪 Testing Your Setup

### **Connection Test**
```javascript
// Test if your app can connect to Supabase
const result = await window.testSupabase.testConnection();
console.log(result);
```

### **Database Test**
```javascript
// Test if you can read/write to your database
const result = await window.testSupabase.testDatabase();
console.log(result);
```

## 🚨 Troubleshooting

### **Common Issues**

1. **"Supabase not configured" error**
   - Check that your credentials are correct in `src/config/supabase.js`
   - Verify your project URL and anon key

2. **"Table doesn't exist" error**
   - Create the required tables in your Supabase dashboard
   - Use the SQL commands above

3. **"Permission denied" error**
   - Enable Row Level Security (RLS) on your tables
   - Create appropriate RLS policies

4. **"Invalid API key" error**
   - Verify your anon key is correct
   - Check that your key hasn't expired

### **Debug Mode**

Enable debug logging in your browser console:

```javascript
// Enable Supabase debug mode
localStorage.setItem('supabase:debug', 'true');
```

## 📱 Features Available

With Supabase connected, you now have access to:

- ✅ **User Authentication** (sign up, sign in, 2FA)
- ✅ **Role-Based Access Control** (admin, manager, supervisor, technician, viewer)
- ✅ **Cloud Data Sync** (assessments, user profiles, teams)
- ✅ **Real-time Updates** (live collaboration)
- ✅ **Secure Data Storage** (encrypted, RLS-protected)
- ✅ **API Endpoints** (RESTful API for integrations)
- ✅ **Audit Logging** (track all user actions)
- ✅ **Team Management** (create teams, manage members)

## 🔐 Security Notes

- **Never expose your service role key** in client-side code
- **Use RLS policies** to control data access
- **Validate all inputs** before sending to database
- **Enable 2FA** for admin accounts
- **Regular security audits** of your policies

## 📞 Support

If you encounter issues:

1. Check the browser console for error messages
2. Verify your Supabase project settings
3. Test the connection using the test utilities
4. Check that all required tables exist
5. Ensure RLS policies are correctly configured

Your Garage RAMS app is now ready to use with Supabase! 🎉
